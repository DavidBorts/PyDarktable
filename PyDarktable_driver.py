import sys
from PyDarktable import functions as f
import PyDarktable as dt

if __name__ != "__main__":
    print('Please run the driver directly. Quitting.')
    quit()

# Command-line format: python PyDarktable_Driver.py <input_image_path> <output_image_path> <intructions_path>
input_image_path = sys.argv[1]      
output_image_path = sys.argv[2]
instructions_path = sys.argv[3]

# Dict of params to fill in
params_dict = {
                'filmicrgb_params': None,
                'colorbalancergb_params': None,
                'sharpen_params': None,
                'exposure_params': None,
                'highlights_params': None,
                'temperature_params': None,
                'raw_prepare_params': None,
            }

# Extracting default raw_prepare and temperature params for image
raw_prepare_params, temperature_params = dt.read_dng_params(input_image_path)
params_dict['raw_prepare_params'] = raw_prepare_params
params_dict['temperature_params'] = temperature_params

# Reading the instructions, line-by-line
with open(instructions_path, 'r') as file:
    instructions = file.readlines()

    for instruction in instructions:
        param, value = instruction.split()

        # Getting the specific collating function for the param's module
        function = getattr(f, param)

        # Collating the new param value with the other parameters for its 
        # module into an instance of a @dataclass
        module_params = function(value)

        # Adding the module params to params_dict
        params_dict[param + "_params"] = module_params
        print(f'setting {param} to {value}.')

        #TODO: Add support for modules with multiple tunable params.
        # Overriding the param string for each instruction would no 
        # longer be suitable.

# Generating the image
dt.render(input_image_path, output_image_path, params_dict)


