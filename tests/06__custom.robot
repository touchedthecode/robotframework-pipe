*** Settings ***
Library     PipeLibrary    pipe_strategy=append    pipe_operator=->    placeholder=_
Resource    keywords.resource

*** Test Cases ***
Pipe Keyword works with custom Placeholder and custom pipe operator
    Pipe    
    ...    Sum    1    2
    ...    ->    Double    _
    ...    ->    Subtract    3
    ...    ->    Should be Equal As Integers    -3    _

