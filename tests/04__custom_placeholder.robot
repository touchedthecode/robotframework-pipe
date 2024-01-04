*** Settings ***
Library     PipeLibrary    placeholder=_
Resource    keywords.resource

*** Test Cases ***
Pipe Keyword works with custom Placeholder
    Pipe    
    ...    Sum    1    2
    ...    >>    Negate    _
    ...    >>    Double    _
    ...    >>    Should be Equal As Integers    -6    _

