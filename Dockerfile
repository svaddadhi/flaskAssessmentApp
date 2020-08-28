FROM python:3.7.4
COPY . /flaskAssessmentApp
WORKDIR /flaskAssessmentApp
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
