*** Settings ***
Library     PipeLibrary
Resource    keywords.resource

*** Test Cases ***
Pipe Keyword works correctly without Placeholder
    Pipe    Sum    1    2    >>    Negate    >>    Double    >>    Should be Equal As Integers    -6

Pipe Keyword works correctly with Placeholder
    Pipe    
    ...    Sum    1    2
    ...    >>    Negate    $
    ...    >>    Double    $
    ...    >>    Should be Equal As Integers    -6    $
    
Pipe Keyword fails on error
    Run Keyword And Expect Error    *    
    ...    Pipe
    ...    Sum    1    2
    ...    >>    Double
    ...    >>    Should be Equal As Integers    0

Pipe Keyword prepends result to arguments by default
    Pipe  
    ...    Sum    1    2
    ...    >>    Subtract    2
    ...    >>    Should be Equal As Integers    1

Pipe Keyword returns value of the last keyword run
    ${sum} =      Pipe    Sum    1    2    >>    Double
    Should Be Equal As Integers    ${sum}    6