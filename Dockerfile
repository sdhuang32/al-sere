FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY lib ./lib
COPY personaldata ./personaldata
COPY test-input.txt ./

# Unit test section
#
# In case temporary files or testing data are going to be generated,
# we should use a multi-stage build and exclude those files to reduce
# the final image size.
RUN python -m lib.deserialiser.torture
RUN python -m lib.serialiser.torture
RUN python -m personaldata.torture

CMD [ "sh" ]
