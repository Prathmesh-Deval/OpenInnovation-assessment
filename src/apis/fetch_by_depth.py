from flask import request, jsonify, render_template, send_file
import sqlite3
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
import logging
from flask_restx import Resource, Namespace

def apply_color_map(values):
    """
    Apply a 'viridis' color map to the values.
    """
    viridis = np.array([
        [68, 1, 84], [69, 3, 87], [70, 6, 90], [71, 8, 93], [72, 11, 95],
        # Include all 256 RGB values from the 'viridis' colormap here...
        [252, 253, 191], [253, 255, 191]
    ])
    norm = Normalize(vmin=0, vmax=255)
    indices = norm(values) * 255
    return viridis[indices.astype(int)]

ns_app = Namespace('')

@ns_app.route('/app')
class App(Resource):
    def get(self):
        return render_template('index.html')

@ns_app.route('/color_map', methods=['GET'])
class App2(Resource):
    def get(self):
        try:
            depth_min = float(request.args.get('depth_min'))
            depth_max = float(request.args.get('depth_max'))

            conn = sqlite3.connect('/src/image_data.db')
            query = "SELECT * FROM resized_images WHERE depth BETWEEN ? AND ?"
            df = pd.read_sql_query(query, conn, params=(depth_min, depth_max))
            conn.close()

            # Extract pixel data and apply color map
            pixel_data = df.iloc[:, 1:].values
            color_mapped_data = np.apply_along_axis(apply_color_map, 1, pixel_data)

            # Convert color-mapped data to an image
            color_mapped_data = (color_mapped_data * 255).astype(np.uint8)
            image = Image.fromarray(color_mapped_data, 'RGB')

            # Save the image to a BytesIO object
            img_io = BytesIO()
            image.save(img_io, format='PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png')
        except Exception as e:
            logging.error(f"Error fetching image frames: {e}")
            return jsonify({"error": "Internal Server Error"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
#

#
#     def post(self):
#         try:
#             depth_min = float(request.args.get('depth_min'))
#             depth_max = float(request.args.get('depth_max'))
#
#             conn = sqlite3.connect('/src/image_data.db')
#             query = "SELECT * FROM resized_images WHERE depth BETWEEN ? AND ?"
#             df = pd.read_sql_query(query, conn, params=(depth_min, depth_max))
#             conn.close()
#
#             # Extract pixel data and apply color map
#             pixel_data = df.iloc[:, 1:].values
#             color_mapped_data = np.apply_along_axis(apply_color_map, 1, pixel_data)
#
#             # Create image from color mapped data
#             fig, ax = plt.subplots(figsize=(10, len(df) * 0.1))
#             ax.imshow(color_mapped_data, aspect='auto')
#             ax.axis('off')
#
#             # Save the image to a BytesIO object
#             img_io = BytesIO()
#             plt.savefig(img_io, format='png', bbox_inches='tight')
#             img_io.seek(0)
#             plt.close(fig)
#
#             return send_file(img_io, mimetype='image/png')
#         except Exception as e:
#             logging.error(f"Error fetching image frames: {e}")
#             return jsonify({"error": "Internal Server Error"}), 500
#
