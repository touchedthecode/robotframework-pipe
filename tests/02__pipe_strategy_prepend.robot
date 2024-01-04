*** Settings ***
Library     PipeLibrary    pipe_strategy=prepend
Resource    keywords.resource

*** Variables ***
${test}    abc

*** Test Cases ***
Pipe Keyword should prepend result to arguments
    Pipe  
    ...    Sum    1    2
    ...    >>    Subtract    2
    ...    >>    Should be Equal As Integers    1