FROM quay.io/azavea/raster-vision:pytorch-0.12

# Uncomment if you add any non-RV requirements.
# COPY ./rastervision_ArcheoStructures_RV/requirements.txt /opt/src/requirements.txt
# RUN pip install $(grep -ivE "rastervision_*" requirements.txt)

COPY ./rastervision_ArcheoStructures_RV/ /opt/src/rastervision_ArcheoStructures_RV/

ENV PYTHONPATH=/opt/src/rastervision_ArcheoStructures_RV/:$PYTHONPATH

CMD ["bash"]
