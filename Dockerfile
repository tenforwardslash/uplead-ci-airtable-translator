FROM python:3.7-slim

VOLUME /data

RUN pip install pandas

ADD translate_uplead_to_ci.py /translate_uplead_to_ci.py
RUN chmod +x /translate_uplead_to_ci.py


ENTRYPOINT ["/translate_uplead_to_ci.py"]