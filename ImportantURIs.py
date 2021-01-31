IMAGERY_URI = "/home/jameszd/Pictures/Satellite_Imagery/Digital_Globe_Foundation_JamesWork/Processed"
LABELS_URI = "/home/jameszd/DissertationProjects/DissertationCode/LabelData"
OUTPUT_URI = "/home/jameszd/DissertationProjects/DissertationCode/output"


sudo docker run --runtime=nvidia -it --ipc=host -v ${ARCH_STRUCT_DATA_DIR}:/opt/data archstruct
#To run it on docker
export ARCH_STRUCT_DATA_DIR="/home/jameszd/DissertationProjects/ArchaeoStruct"
docker/run [--gpu][--tensorboard]

export RAW_URI="/opt/data/Imagery"
export PROCESSED_URI="/opt/data/Processed"
export ROOT_URI="/opt/data/output"

rastervision run local rastervision.ArcheoStructures_RV.ArchaeoStruct_Pipeline \
-a raw_uri $RAW_URI -a processed_uri $PROCESSED_URI -a root_uri $ROOT_URI \
-a test True


#To run example on docker
export ARCH_STRUCT_DATA_DIR="/home/jameszd/DissertationProjects/ExampleForTesting"
docker/run [--gpu][--tensorboard]

export RAW_URI="/opt/data/Imagery"
export PROCESSED_URI="/opt/data/Processed"
export ROOT_URI="/opt/data/output"

rastervision run local rastervision.ArcheoStructures_RV.ArchaeoStruct_Pipeline \
-a raw_uri $RAW_URI -a processed_uri $PROCESSED_URI -a root_uri $ROOT_URI \
-a test False --splits=2
