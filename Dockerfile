FROM python:2.7

# install dependencies
RUN pip install -r https://raw.githubusercontent.com/dnouri/nolearn/0.6.0/requirements.txt
RUN pip install nolearn
RUN pip install tqdm
RUN pip install flask

RUN apt update
RUN apt-get --yes install default-jre
RUN apt-get --yes install bedtools
RUN apt-get --yes install bowtie2
RUN apt-get --yes install samtools


# get deepARG source code
# RUN rm -r /bin/deeparg-ss
RUN test -d /deeparg && echo "/deeparg exits: removing" && rm -r /deeparg || echo "done"
RUN test -d ./deeparg-ss && echo "./deeparg-ss exits: removing" && rm -r ./deeparg-ss || echo "done"

COPY ./ /deeparg
# RUN git clone https://gaarangoa@bitbucket.org/gusphdproj/deeparg-ss.git && mv ./deeparg-ss /deeparg

RUN chmod +x /deeparg/bin/diamond

# docker-compose -f build_deeparg_image.yaml build
# docker-compose -f build_deeparg_image.yaml up -d
# docker commit deepARG gaarangoa/deeparg:latest
# docker push gaarangoa/deeparg:latest