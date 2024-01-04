*** Settings ***
Library     PipeLibrary    pipe_strategy=append
Resource    keywords.resource

*** Test Cases ***
Pipe Keyword should append result to arguments
    Pipe  
    ...    Sum    1    2
    ...    >>    Subtract    2
    ...    >>    Should be Equal As Integers    -1