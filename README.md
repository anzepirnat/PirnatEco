# Towards Sustainable Deep Learning for Wireless Fingerprinting Localization

### [Paper](https://ieeexplore.ieee.org/document/9838464) | [Data](https://data.ieeemlc.org/Ds1Detail)

[![Explore Siren in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anzepirnat/PirnatEco/blob/main/WholeCode.ipynb)<br>

[Anže Pirnat](https://sensorlab.ijs.si/people/apirnat/)\*,
[Blaž Bertalanič](https://sensorlab.ijs.si/people/bbertalanic/)\,
[Gregor Cerar](https://sensorlab.ijs.si/people/gcerar/),
[Mihael Mohorčič](https://sensorlab.ijs.si/people/mmohorcic/),
[Marko Meža](https://www.fe.uni-lj.si/o_fakulteti/imenik_zaposlenih/po_abecedi/199/),
[Carolina Fortuna](https://sensorlab.ijs.si/people/cfortuna/)<br>
Sensorlab, Jozef Stefan Institute

## Google Colab
If you want to try out the code or experiment with the model, we have written a [Colab](https://colab.research.google.com/github/anzepirnat/PirnatEco/blob/main/WholeCode.ipynb). 

Model PirnatEco can be found in PirnatEco.ipynb. The whole code needed to run the model, link to the dataset CTW2019 and the model is in the WholeCode.ipynb and is deployable through the colab link above the text.

There is also a code for a webapp that calculates complexity of the DL model with equations used and presented in the paper.

## Getting started
If you wanna recreate the experiment the first step is to download data from the [original source](https://data.ieeemlc.org/Ds1Detail) in the format .hdf5. After that save it to google drive with path MyDrive/CTW2019_h5/ . Then click on the 'open in colab' button and run the code as you please. If you have any question we are happy to answer them.

### Requirements
The last cell of WholeCode.ipynb displays the requirements needed for running the code. Additionally, a requirements.txt file is also provided which includes all the dependencies installed by Colab, including those not used in the code.

## Citation

If you find our work useful in your research, please cite: [Towards Sustainable Deep Learning for Wireless Fingerprinting Localization](https://ieeexplore.ieee.org/document/9838464).
If you are using the support code in WholeCode, citation of [Improving CSI-based Massive MIMO Indoor Positioning using Convolutional Neural Network](https://arxiv.org/abs/2102.03130) would be greatly appreciated.

### Acknowledgement

The research leading to these results has received funding from the Slovenian Research Agency under Communication Systems Program (P2-0016).
