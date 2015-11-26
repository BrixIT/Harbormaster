FROM python:3.5-onbuild
# docker run -p 5000:5000 -v /var/run/docker.sock:/docker.sock harbormaster
EXPOSE 5000
CMD ["python", "./runserver.py"]
