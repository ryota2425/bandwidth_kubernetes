FROM ubuntu:18.04
#install basics
RUN apt update -y
RUN apt-get install -y apt-utils git curl ca-certificates bzip2 cmake tree htop bmon iotop g++
RUN apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev python-pip python3-pip


RUN pip3 install -U pip
#RUN pip3 install bluepy
#RUN apt-get install -y git build-essential libglib2.0-dev
#RUN python3 -m pip install time
#RUN python3 -m pip install statistics


#RUN python3 -m pip install elasticsearch==7.9.1
#RUN git clone https://github.com/IanHarvey/bluepy.git && cd bluepy && python3 setup.py build && python3 setup.py install
#RUN rm -r bluepy

RUN pip3 install prometheus_client
#RUN pip3 install subprocess

RUN apt-get install -y wget
RUN ls
RUN wget https://gist.githubusercontent.com/ryota2425/42220c99a379c0a23e1b388f4dcfd24f/raw/55ae060bc81b0cde772cc5f80473a055b33cfc98/bandwidth_server.py -O temp.py
#COPY temp2.py ./
RUN pip3 install iperf3
RUN git clone https://github.com/esnet/iperf.git &&  cd iperf && ./configure; make; make install && cd  /usr/local/lib/ && ldconfig
CMD python3 temp.py
