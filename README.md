# DFRobot_IMU_Show

<img src="./image/imu_show.gif">

## usage

The textbox on the right of the interface will show the uploaded data. <br>
And the left  of the interface is a 3d cube. <br>
The top of the cube is red, the bottom is green, the left is blue, the right is yellow, the front is cyan, the back is pink. <br>
<br>
If the received data (attitude data) satisfies the following format: <br>
Pitch:xxx.xx roll:xxx.xx yaw:xxx.xx ...'\n' <br>
Example: pitch:32.12 roll:124.2145 yaw:1.057 '\n' <br>
<br>
Then the cube will be rotated in the data format 
<br>

## Compatibility


system                | Work Well | Work Wrong | Untested  | Remarks
------------------ | :----------: | :----------: | :---------: | -----
win7 64  |      √       |             |            | 
win7 32  |      √       |             |            | 
win8 64 |       √      |             |            | 
win8 32 |             |             |      √      | 
win10 64 |      √       |             |            | 
win10 32 |      √       |             |            | 
