//12-5-2026: Tokenize Struct

//pragma once om header max 1x te includeren
#pragma once
#include <string>
#include <vector>

enum class TokenType
{
    // Selectie van woorden die we kunnen maken
    WORD,
    PHRASE,
    AND,
    OR,
    COMMAND
};

struct Token
{
    TokenType type;
    std::string value;
};

std::vector<Token> tokenizeQuery(const std::string& input);

