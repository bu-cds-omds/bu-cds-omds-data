#!/usr/bin/env python3

# This script pulls the Abalone data set from the UC Irvine Machine
# Learning Repository.
#
# https://archive.ics.uci.edu/dataset/1/abalone
#
# Nash,Warwick, Sellers,Tracy, Talbot,Simon, Cawthorn,Andrew, and Ford,Wes. (1995). Abalone. UCI Machine Learning Repository.
# https://doi.org/10.24432/C55C7W.

from ucimlrepo import fetch_ucirepo

abalone = fetch_ucirepo(id=1)

abalone.data.original.to_csv(path_or_buf="data/abalone.tsv", index=False, sep="\t")
