#!/bin/bash

awk '
    /^>/ {
        if (first) {
            printf "%s\n", $0; 
            first = 0
        } else {
            printf "\n%s\n", $0
        }
        next
    }
    {
        printf "%s", toupper($0)
    }
' first=1 ${PWD}/mock_NCBI.fasta > "fixed.fasta"

