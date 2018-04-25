---
layout: post
title: "B22. Simulating In Vivo-Like States for Hippocampal CA1 Interneuron Specific 3 Cells"
header-img: "img/banner.jpg"
category: abstracts
platform: "neuro"
subtitle: "Alexandre Guet-McCreight, Lisa Topolnik, Frances K. Skinner"
tags: poster neuro
session_id: B22 Poster_Session_2
visible: true
---
Poster_Session_2 - B22

**<sup>1,2</sup>Alexandre Guet-McCreight**, <sup>3,4</sup>Lisa Topolnik, <sup>1,5,2</sup>Frances K. Skinner

__1 Krembil Research Institute, University Health Network; 2 Dept. of Physiology, University of Toronto; 3 Centre de recherche de l’institut universitaire en santé mentale de Québec, Université Laval; 4 Biochemistry, Microbiology and Bioinformatics, Université Laval; 5 Medicine (Neurology), University of Toronto__

Obtaining recordings from individual cells during behaviour is technically challenging. This is more so for hippocampal interneuron subtypes which represent a neuronal minority and are difficult to unambiguously identify given interneuron diversities. Interneuron specific 3 (IS3) cells, a cell type known to exclusively inhibit other inhibitory interneurons, has yet to be characterized in terms of its function in vivo. Our goal here is to generate in vivo-like states for IS3 cells using our previously developed IS3 cell models to predict inputs that they receive in vivo and, in concert with experiment, to understand their functional contributions to hippocampal activity.
We know that neurons in vivo show more depolarized membrane potentials (Vm), increased Vm standard deviations (σVm), and increased irregular spiking as measured by the coefficient of variation of interspike intervals (ISICV) relative to those in vitro. We use these criteria to determine conditions under which our models can exhibit high-conductance (HC), or in vivo-like, states. We started with two previously developed multi-compartment models of IS3 cells, experimentally-constrained synaptic parameters, and realistic synaptic density values. The first model variant (SDprox1), possesses ion channels in the soma and proximal dendrites including A-type potassium channels (IA), whereas in the second model variant (SDprox2), IA is restricted to the soma.
We perform a parameter search where we vary the full range of synapse numbers and a wide range of presynaptic spike rates (~4.4 million simulations). We find that synchronous inputs (mainly excitatory) amplify the size of the HC state parameter spaces through increased ISICV and σVm values. On dividing the parameter space into high/low pools, we find that having (i) high excitation (783-1530 synapses; 20-30 Hz) and low inhibition (4-172 synapses; 10-50 Hz), or (ii) high inhibition (176-344 synapses; 60-100 Hz) and low excitation (18-765 synapses; 5-15 Hz), shifts the parameter space away from HC regimes. Also, SDprox2 mostly generated larger numbers of HC scenarios, likely due to the SDprox1 model having dendritic IA, which reduces excitability.
Thus, we have shown that common inputs, balanced excitation/inhibition, and lack of dendritic IA, promote HC states in IS3 cell models. We can further reduce possible HC scenarios by excluding levels of synaptic input that would render distal dendrites unresponsive due to saturation, and examining responsiveness to rhythmic inputs. Moving forward, these models will be used in combination with experimental work to obtain an understanding of the functional roles of IS3 cells in the hippocampus.