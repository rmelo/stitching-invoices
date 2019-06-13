FROM hulkinbrain/docker-opencv2
ADD ./src
ADD ./resources
RUN echo "Hello World!"
