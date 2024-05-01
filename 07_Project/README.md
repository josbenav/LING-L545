# A Constraint Grammar disambiguator for Hnaring Lutuv (Lautu Chin)

This paper presents ongoing work on a finite-state transducer, morphological analyser, and a Constraint Grammar disambiguation tool designed for Hnaring Lutuv (Lautu Chin `ISO 639-3 clt`). Lutuv is a Tibeto Burman language with a high degree of ambiguity both in the lexicon and in the case marking system. The performance of the disambiguation tool composed of 73 rules was evaluated against a sample dataset showing that the system outperforms the process of manual disambiguation.

Following work on Breton [^1], the morphological analyzer and disambiguator for Lutuv will be created using Apertium, a free/open-source (FOS) machine translation (MT) platform that consist of an engine, a toolbox, and data to build rule-based MT systems[^2]. Apertium is a growing community-driven project that has released more than 30 language pairs, including Spanish-Portuguese, English-Catalan, Basque-English, among many others. 

The proposed constraint grammar disambiguation tool comprises 73 rules divided into three main categories: _Safe_, _Safe heuristic_, and _Heuristic_[^3]. The concept of Safe is meant to represent real constraints in the language. For instance, a subject agreement marker must occur immediately before the verb. On the other hand, Safe heuristic rules deal with highly frequent tendencies in the language. For example, the majority of times the locative markers occur immediately after a noun. Finally, Heuristic rules are those expressing preferences, but they do not consider linguistic constraints. For instance, nouns are marked with either a focus or a topic marker.

After the disambiguation rule set for Lutuv was created, the performance of the rule set was evaluated using the script `vislcg3-evaluate.py` available [here](https://github.com/ftyers/ud-scripts/blob/master/vislcg3-evaluate.py). The script measures the precision and recall of each rule to disambiguate the sample dataset that was manually disambiguated before. Thus, the evaluation takes both files the raw input sentences and the manually disambiguated sentences. The results show that the rule set is of high precision, **0.98**, a recall value of **0.93**, against an input ambiguity of **1.72**, a reference ambiguity of **1.69**, and an output ambiguity of **1.03**. 

## Documentation

Find all the documentation used in this project in [this](https://github.com/josbenav/apertium-clt/tree/master) repository.

## Relevant files

Find the following files in this folder: 

- Rule set: `apertium-clt.clt.rlx`
- Disambiguation results: `lau_dis_results.txt`
- Input sentences: `lau_raw_sent_dis.txt`
- Manual disambiguation: `lau_manual_dis.txt`

### Practical codes

To check the morphology: `echo (Lutuv sentence) | apertium -d . clt-morph | cg-conv`

To check the disambiguation: `echo Lutuv sentence | apertium -d. clt-disam`

## References
[^1]: Francis M Tyers and Nick Howell. 2021. Morphological analysis and disambiguation for breton. _Language Resources and Evaluation_, 55:431–473

[^2]: Mikel L Forcada, Mireia Ginestí-Rosell, Jacob Nordfalk, Jim O’Regan, Sergio Ortiz-Rojas, Juan Antonio Pérez-Ortiz, Felipe Sánchez-Martínez, Gema
Ramírez-Sánchez, and Francis M Tyers. 2011. Apertium: a free/open-source platform for rule-based machine translation. _Machine translation_, 25:127–144

[^3]: Francis M Tyers and Robert Reynolds. 2015. A preliminary constraint grammar for russian. In Proceedings of the workshop on _"Constraint Grammar—methods, tools and applications"_, pages 39–46.

