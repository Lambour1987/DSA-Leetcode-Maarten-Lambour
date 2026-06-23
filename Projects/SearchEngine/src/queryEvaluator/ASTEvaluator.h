// 4-6-2026

// Voorkom dat headers vaker ingeladen worden
#pragma once

// Voeg een map, set en string toe
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <cmath>

// Verwijs naar AST.h
#include "../types/AST.h"

// Maak een alias voor die hashmap string, set (van strings) en noem die InvertedIndex
// gewijzigd: using InvertedIndex = std::unordered_map<std::string, std::unordered_set<std::string>>;
using InvertedIndex = std::unordered_map<std::string, std::unordered_map<std::string, std::vector<int>>>;

// maak een functie evaluateAST met als parameters een pointer node naar een ASTNode, en
// de index (map incl set: maar gebruik de alias). Als output een set van strings
// 17-6-2026: we maken van de functie nu een class std::unordered_map<std::string,double> evaluateAST(ASTNode* node, const InvertedIndex& index);

class ASTEvaluator
{
    private:

        int totalDocs;

        std::unordered_map<std::string,int>docLength;

        double avgDocLen;

        double k1 = 1.5;
        double b = 0.75;

        double computeIDF(int N, int df);

    public:
        // Dit is de Constructor
        ASTEvaluator(
            int totalDocs,
            const std::unordered_map<std::string,int>& docLength);

        std::unordered_map<std::string,double>evaluateAST(ASTNode*node, const InvertedIndex& index);

};


