*** Settings ***
Library     PipeLibrary    pipe_operator=->
Resource    keywords.resource

*** Test Cases ***
Pipe Keyword works with custom pipe operator
    Pipe    Sum    1    2    ->    Negate    ->    Double    ->    Should be Equal As Integers    -6