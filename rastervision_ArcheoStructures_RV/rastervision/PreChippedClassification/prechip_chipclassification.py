import logging

import numpy as np
import pdb
from rastervision.core.rv_pipeline.chip_classification import ChipClassification
from rastervision.core.box import Box

log = logging.getLogger(__name__)

def get_train_windows(scene):
    # pdb.set_trace()
    labels = scene.ground_truth_label_source.get_labels()
    train_windows=labels.get_cells()
    return train_windows

class PrechipChipClassification(ChipClassification):
    def get_train_windows(self,scene):
        return get_train_windows(scene)
