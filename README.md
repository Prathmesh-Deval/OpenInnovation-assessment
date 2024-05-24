# Open Innovation Assessment

#### Attached is a csv file that contains image data referenced by the column depth. The rest of columns (200) represent image pixel values from 0 to 255 at each depth.
#### You can find solution for respective challenges in below files:


#### File Descriptions

| File Path                      | Description                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| src/image_preprocess.py        | The image size is relatively big. Hence, there is a need to resize the image width to 150 instead of 200. |
| src/services/database.py       | The resized image has to be stored in a database.                                            |
| src/apis/fetch_by_depth.py     | An API is required to request image frames based on depth_min and depth_max. <br> Apply a custom color map to the generated frames. |

<br>
The solution should be based on Python.<br>
deployment of the solution in a cloud service : serverless deployment


Thanks!