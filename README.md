# PyDarktable
##### _A Python Wrapper for Darktable's CLI_


&nbsp;
Use _PyDarktable_driver.py_ for a simlple means of interfacing with the code.

Command format:
```sh
python PyDarktable_driver.py <image_input_path> <image_output_path> <instructions_path>
```

### Instructions

Instructions for the driver are written in a _.txt_ file, with each instruction as a separate line.
| Instruction | range |
| ------ | ------ |
| colorbalancergb (_contrast_) | [-0.9, 0.9]
| sharpness | [0.0, 10.0] 
| exposure | [-2.0, 4.0]
An example:
```sh
sharpness 5.0
exposure 2.37
colorbalancergb 0.17
...
<param_name> <value>
```
The order of the instructions does not matter