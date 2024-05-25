from flask import request, jsonify, render_template, send_file, make_response
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from io import BytesIO
import logging
from flask_restx import Resource, Namespace
import matplotlib
matplotlib.use('Agg')

ns_app = Namespace('')


def apply_color_map(values):
    norm = Normalize(vmin=0, vmax=255)
    return plt.cm.viridis(norm(values))[:, :3]


@ns_app.route('/app')
class App(Resource):
    def get(self):
        return make_response(render_template('index.html'))


@ns_app.route('/color_map', methods=['GET'])
class App2(Resource):
    def get(self):
        try:
            depth_min = float(request.args.get('depth_min'))
            depth_max = float(request.args.get('depth_max'))

            conn = sqlite3.connect('/Users/prdeval/Desktop/Projects/openinnovation/app/services/image_data.db')
            query = "SELECT * FROM resized_images WHERE depth BETWEEN ? AND ?"
            df = pd.read_sql_query(query, conn, params=(depth_min, depth_max))
            conn.close()

            if df.empty:
                return jsonify({"message": "Depth range not found. Please try a range between 9000.1 and 9546.0"})

            pixel_data = df.iloc[:, 1:].values
            color_mapped_data = np.apply_along_axis(apply_color_map, 1, pixel_data)

            fig, ax = plt.subplots(figsize=(10, len(df) * 0.1))
            ax.imshow(color_mapped_data, aspect='auto')
            ax.axis('off')

            img_io = BytesIO()
            plt.savefig(img_io, format='png', bbox_inches='tight')
            img_io.seek(0)
            plt.close(fig)

            return send_file(img_io, mimetype='image/png')
        except Exception as e:
            logging.error(f"Error fetching image frames: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
