[![banner](assets/banner.png)](http://introtodeeplearning.com)

This repository contains all of the code and software labs for [MIT Introduction to Deep Learning](http://introtodeeplearning.com)! All lecture slides and videos are available on the program website.

# Instructions
MIT Introduction to Deep Learning software labs are designed to be completed at your own pace. At the end of each of the labs, there will be instructions on how you can submit your materials as part of the lab competitions. These instructions include what information must be submitted and in what format.

## Opening the labs in Google Colaboratory:

The 2023 Introduction to Deep Learning labs can be run in Google's Colaboratory, a Jupyter notebook environment that runs entirely in the cloud, so you don't need to download anything. To run these labs, you must have a Google account.

On this Github repo, navigate to the lab folder you want to run (`lab1`, `lab2`, `lab3`) and open the appropriate python notebook (\*.ipynb). Click the "Run in Colab" link on the top of the lab. That's it!

## Opening the labs in Intel Dev Cloud:

The labs can also be run in Intel's Dev Cloud.
Follow the [instructions to get access to the Intel Dev Cloud](https://github.com/bjodom/idc) 
and then after logging into the system,
run the following commands in your shell (on the head node is ok, the user files are shared),
which will pull in a version of the files in this course adapted for Intel.  
```bash
git clone https://github.com/mmccool/introtodeeplearning.git
python -m pip install ./introtodeeplearning
```
Then, add the following to the end of your `.bashrc`:
```bash
export PATH=\"$HOME/.local/bin:$PATH
source /opt/intel/oneapi/setvars.sh
export ONEAPI_DEVICE_SELECTOR="level_zero:gpu"
conda activate tensorflow_xpu
```
This will force use of the Intel XPUs.
You can leave out the conda activation and do it manually if you want but for this course this
is what will be used.  You can also check the number and kind of available devices with the 
`sycl-ls` command.

Note: If you installed a previous version of these labs (including by trying to step through the labs before setting up from the alternative repo above) you may have to run the following command first to clean out the old install:
```bash
pip uninstall mitdeeplearning
```

Now log back out, then back in, and start a Jupyter server as described in the instructions.

In the labs themselves, the pip command to install the `mitdeeplearning` package will do
nothing since it's already installed above.
You may also want to comment out the "magic function" starting with `%`.
In Google Colab this is used to select the tensorflow version but we have also already
done that as part of the conda environment activation above.

## Running the labs
Now, to run the labs, open the Jupyter notebook as described above. 

On the Intel Dev Cloud, the above setup is used to select the XPU for execution.

On Google Colab, navigate to the "Runtime" tab --> "Change runtime type". In the pop-up window, under "Runtime type" select "Python 3", and under "Hardware accelerator" select "GPU". 

Go through the notebooks and fill in the `#TODO` cells to get the code to compile for yourself!

### MIT Deep Learning package
You might notice that inside the labs we install the `mitdeeplearning` python package from the Python Package repository:

`pip install mitdeeplearning`

This package contains convienence functions that we use throughout the course and can be imported like any other Python package.

`>>> import mitdeeplearning as mdl`

We do this for you in each of the labs, but the package is also open source under the same license so you can also use it outside the class.

## Lecture Videos

[<img src="assets/video_play.png" width="500">](https://www.youtube.com/watch?v=njKP3FqW3Sk&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI&index=1)

All lecture videos are available publicly online and linked above! Use and/or modification of lecture slides outside of MIT Introduction to Deep Learning must reference:

> © MIT Introduction to Deep Learning
>
> http://introtodeeplearning.com

## License
All code in this repository is copyright 2023 [MIT Introduction to Deep Learning](http://introtodeeplearning.com). All Rights Reserved.

Licensed under the MIT License. You may not use this file except in compliance with the License. Use and/or modification of this code outside of MIT Introduction to Deep Learning must reference:

> © MIT Introduction to Deep Learning
>
> http://introtodeeplearning.com
