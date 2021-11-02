FROM agrigorev/zoomcamp-model:3.8.12-slim

ENV PYTHONUNBUFFERED=TRUE

RUN pip install --upgrade pip 
RUN pip --no-cache-dir install pipenv

WORKDIR /app

COPY . .

RUN pipenv install --deploy --system && rm -rf /root/.cache

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:9696", "predict:app" ]