from spynnaker_extra_pynn_models import model_binaries

# spynnaker 8 extra models
from spynnaker8_extra_pynn_models.neuron.builds\
    .if_cond_exp_stoc_data_holder import IfCondExpStocDataHolder \
    as IFCondExpStock
from spynnaker8_extra_pynn_models.neuron.builds\
    .if_curr_delta_data_holder import IfCurrDeltaDataHolder as \
    IFCurDelta
from spynnaker8_extra_pynn_models.neuron.builds\
    .if_curr_exp_ca2_adaptive_data_holder import \
    IfCurrExpCa2AdaptiveDataHolder as IFCurrExpCa2Adaptive

# plastic timing spynnaker 8
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_recurrent \
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_spike_nearest_pair import \
    TimingDependenceSpikeNearestPair
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_vogels_2011 \
    import TimingDependenceVogels2011 as Vogels2011Rule
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet

# plastic weight spynnaker 8
from spynnaker8_extra_pynn_models.neuron.plasticity.stdp.weight_dependence \
    .weight_dependence_additive_triplet import \
    WeightDependenceAdditiveTriplet

__all__ = [
    # spynnaker 8 models
    'IFCurDelta', 'IFCurrExpCa2Adaptive', 'IFCondExpStock',

    # spynnaker 8 plastic stuff
    'WeightDependenceAdditiveTriplet',
    'TimingDependencePfisterSpikeTriplet',
    'TimingDependenceSpikeNearestPair',
    'RecurrentRule', 'Vogels2011Rule']


def _init_module():
    # import logging
    import os
    from spynnaker.pyNN.spinnaker_common import SpiNNakerCommon

    # Register this path with SpyNNaker
    SpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
