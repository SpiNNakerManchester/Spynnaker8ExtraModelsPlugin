from spynnaker.pyNN.abstract_spinnaker_common import AbstractSpiNNakerCommon

from spynnaker_extra_pynn_models import model_binaries

# spynnaker 8 extra models
from spynnaker8_extra_pynn_models.neuron.builds\
    import IfCondExpStocDataHolder as IFCondExpStock
from spynnaker8_extra_pynn_models.neuron.builds\
    import IfCurrDeltaDataHolder as IFCurDelta
from spynnaker8_extra_pynn_models.neuron.builds\
    import IfCurrExpCa2AdaptiveDataHolder as IFCurrExpCa2Adaptive

# plastic timing spynnaker 8
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceSpikeNearestPair as SpikeNearestPair
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependenceVogels2011 as Vogels2011Rule
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    import TimingDependencePfisterSpikeTriplet as PfisterSpikeTriplet

# plastic weight spynnaker 8
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.weight_dependence \
    import WeightDependenceAdditiveTriplet

import os

__all__ = [
    # spynnaker 8 models
    'IFCurDelta', 'IFCurrExpCa2Adaptive', 'IFCondExpStock',

    # spynnaker 8 plastic stuff
    'WeightDependenceAdditiveTriplet',
    'PfisterSpikeTriplet',
    'SpikeNearestPair',
    'RecurrentRule', 'Vogels2011Rule']


def _init_module():

    # Register this path with SpyNNaker
    AbstractSpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
