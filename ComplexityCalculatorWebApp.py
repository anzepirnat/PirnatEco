from __future__ import barry_as_FLUFL
from cProfile import run
from pyrsistent import v
import streamlit as st
from PIL import Image


st.title("COMPLEXITY CALCULATOR")
st.write("Everything is calculated as if you are using ReLU activation function, if you aren't, the results will be off a bit.")



#sidebar
st.sidebar.header("about")
st.write("For more information please check out our [paper](https://www.researchgate.net/publication/358144939_Towards_Sustainable_Deep_Learning_for_Wireless_Fingerprinting_Localization). If you are using our calculator in research, citation of the paper would be greatly appreciated.")
st.sidebar.text("This is a calculator with which you")
st.sidebar.text("can calculate the complexity of ")
st.sidebar.text("machine/deep learning architectures.")
st.sidebar.text("It calculates the complexity of 3")
st.sidebar.text("most complexity inducing layers: ")
st.sidebar.text("fully-connected/dense layer,")
st.sidebar.text("convolutional layer,")
st.sidebar.text("pooling layer")


# FULLY CONNECTED
st.header("Fully-connected layer")
# video
vid1_file = open("FullyConnectedLayer.mp4", "rb").read()
st.video(vid1_file)
#image
Timg = Image.open("input_tensorWebApp.jpg")
st.image(Timg)
#vnos
#number input
Fchannels = st.number_input("channels", key="Fchannels", step=1)
Finput_rows = st.number_input("input rows", key="Finput_rows", step=1)
Finput_cols = st.number_input("input columns", key="Finput_cols", step=1)
# image
Fimg = Image.open("basicFClayerWebApp.jpg")
st.image(Fimg)
# code
Foutput_size = st.number_input("output size", key="Foutput_size", step=1)
# predpona
Fpotenca = st.select_slider(
     'Unit of output:',
     options=['FLOPs', 'kFLOPs', 'MFLOPs', 'GFLOPs', 'TFLOPs'], key="Fpotenca")
#channels = 16
#input_rows = 37
#input_cols = 37
#output_size = 64

if st.button("submit"):
    if (Fchannels == 0 or Finput_rows == 0 or Finput_cols == 0 or Foutput_size == 0):
        st.warning("none of the inputs should be equal to 0")
    F_total_flops_per_layer = 2 * Fchannels * Finput_rows * Finput_cols * Foutput_size + Foutput_size
    if (Fpotenca == 'FLOPs'):
        st.success(F_total_flops_per_layer)
    if (Fpotenca == 'kFLOPs'):
        st.success(F_total_flops_per_layer/1000)
    if (Fpotenca == 'MFLOPs'):
        st.success(F_total_flops_per_layer/1000000)
    if (Fpotenca == 'GFLOPs'):
        st.success(F_total_flops_per_layer/1000000000)
    if (Fpotenca == 'TFLOPs'):
        st.success(F_total_flops_per_layer/1000000000000)



# CONVOLUTIONAL
st.header("Convolutional layer")
# video
vid2_file = open("ConvolutionalLayer.mp4", "rb").read()
st.video(vid2_file)
#image
Timg = Image.open("input_tensorWebApp.jpg")
st.image(Timg)
# code
# code
#num_filters=16
#channels=32
#input_rows=75
#input_cols=75
#kernel_rows=7
#kernel_cols=7
#stride_rows = 1
#stride_cols = 1
Cchannels = st.number_input("channels", key="Cchannels", step=1)
Cinput_rows = st.number_input("input rows", key="Cinput_rows", step=1)
Cinput_cols = st.number_input("input columns", key="Cinput_cols", step=1)
# image
Cimg = Image.open("convolutionalWebApp.jpg")
st.image(Cimg)
# code
Cnum_filters = st.number_input("number of filters aka. kernels", key="Cnum_filters", step=1)
Ckernel_rows = st.number_input("kernel rows", key="Ckernel_rows", step=1)
Ckernel_cols = st.number_input("kernel columns", key="Ckernel_cols", step=1)
Cstride_rows = st.number_input("stride rows", key="Cstride_rows", step=1)
Cstride_cols = st.number_input("stride columns", key="Cstride_cols", step=1)

Cpadding_rows = (Ckernel_rows - 1) / 2
Cpadding_cols = (Ckernel_cols - 1) / 2
Cinput_shape = (Cchannels,Cinput_rows,Cinput_cols) # Format:(channels, rows,cols)
Cconv_filter = (Cnum_filters,Cchannels,Ckernel_rows,Ckernel_cols)  # Format: (num_filters, channels, rows, cols)


Cpotenca = st.select_slider(
     'Unit of output:',
     options=['FLOPs', 'kFLOPs', 'MFLOPs', 'GFLOPs', 'TFLOPs'], key="Cpotenca")

if st.button("submit", key="Csubmit"):
    if (Cchannels == 0 or Cinput_rows == 0 or Cinput_cols == 0 or Cnum_filters == 0 or Ckernel_rows == 0 or Ckernel_cols == 0 or Cstride_rows == 0 or Cstride_cols == 0):
        st.warning("none of the inputs should be equal to 0")
    n = Cconv_filter[1] * Cconv_filter[2] * Cconv_filter[3]  # tensor size
    Cflops_per_instance = 2*n + 1    # general defination for number of flops (n: multiplications and n-1: additions)
    Cnum_instances_per_filter = (( Cinput_shape[1] - Cconv_filter[2] + 2*Cpadding_rows) / Cstride_rows ) + 1  # for rows
    Cnum_instances_per_filter *= (( Cinput_shape[2] - Cconv_filter[3] + 2*Cpadding_cols) / Cstride_cols ) + 1 # multiplying with cols
    Cflops_per_filter = Cnum_instances_per_filter * Cflops_per_instance
    Ctotal_flops_per_layer = Cflops_per_filter * Cconv_filter[0]    # multiply with number of filters
    Ctotal_flops_per_layer += Cconv_filter[0]*Cnum_instances_per_filter

    if (Cpotenca == 'FLOPs'):
        st.success(Ctotal_flops_per_layer)
    if (Cpotenca == 'kFLOPs'):
        st.success(Ctotal_flops_per_layer/1000)
    if (Cpotenca == 'MFLOPs'):
        st.success(Ctotal_flops_per_layer/1000000)
    if (Cpotenca == 'GFLOPs'):
        st.success(Ctotal_flops_per_layer/1000000000)
    if (Cpotenca == 'TFLOPs'):
        st.success(Ctotal_flops_per_layer/1000000000000)





# POOLING
st.header("Pooling layer")
# video
vid3_file = open("PoolingLayer.mp4", "rb").read()
st.video(vid3_file)
#image
Timg = Image.open("input_tensorWebApp.jpg")
st.image(Timg)
# code
# code
#channels=16
#input_rows=75
#input_cols=75
#kernel_rows=2
#kernel_cols=2
#stride_rows = 1
#stride_cols = 1
Pchannels = st.number_input("channels", key="Pchannels", step=1)
Pinput_rows = st.number_input("input rows", key="Pinput_rows", step=1)
Pinput_cols = st.number_input("input columns", key="Pinput_cols", step=1)
Pimg = Image.open("poolingWebApp.jpg")
st.image(Pimg)
Pkernel_rows = st.number_input("kernel rows", key="Pkernel_rows", step=1)
Pkernel_cols = st.number_input("kernel columns", key="Pkernel_cols", step=1)
Pstride_rows = st.number_input("stride rows", key="Pstride_rows", step=1)
Pstride_cols = st.number_input("stride columns", key="Pstride_cols", step=1)

Ppotenca = st.select_slider(
     'Unit of output:',
     options=['FLOPs', 'kFLOPs', 'MFLOPs', 'GFLOPs', 'TFLOPs'], key="Ppotenca")

if st.button("submit", key="Psubmit"):
    if (Pchannels == 0 or Pinput_rows == 0 or Pinput_cols == 0 or Pkernel_rows == 0 or Pkernel_cols == 0 or Pstride_rows == 0 or Pstride_cols == 0):
        st.warning("none of the inputs should be equal to 0")
    Pinput_shape = (Pchannels,Pinput_rows,Pinput_cols) # Format:(channels, rows,cols)
    Pconv_filter = (Pchannels,Pkernel_rows,Pkernel_cols)  # Format: (num_filters, channels, rows, cols)
    Pn = Pconv_filter[0] * Pconv_filter[1] * Pconv_filter[2]  # tensor size
    Pflops_per_instance = 2*Pn + 1    # general defination for number of flops (n: multiplications and n-1: additions)
    Pnum_instances_per_filter = ((Pinput_shape[1] - Pconv_filter[1]) / Pstride_rows ) + 1  # for rows
    Pnum_instances_per_filter *= ((Pinput_shape[2] - Pconv_filter[2]) / Pstride_cols ) + 1 # multiplying with cols
    P_total_flops_per_layer = Pnum_instances_per_filter * Pflops_per_instance

    if (Ppotenca == 'FLOPs'):
        st.success(P_total_flops_per_layer)
    if (Ppotenca == 'kFLOPs'):
        st.success(P_total_flops_per_layer/1000)
    if (Ppotenca == 'MFLOPs'):
        st.success(P_total_flops_per_layer/1000000)
    if (Ppotenca == 'GFLOPs'):
        st.success(P_total_flops_per_layer/1000000000)
    if (Ppotenca == 'TFLOPs'):
        st.success(P_total_flops_per_layer/1000000000000)
