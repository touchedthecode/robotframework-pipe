*** Keywords ***
Sum
    [Arguments]    ${a}    ${b}
    ${sum} =    Evaluate    ${a} + ${b}
    RETURN    ${sum}

Subtract
    [Arguments]    ${a}    ${b}
    ${value} =    Evaluate    ${a} - ${b}
    RETURN    ${value}

Negate
    [Arguments]    ${num}
    ${product} =    Evaluate    -1 * ${num}
    RETURN    ${product}

Double
    [Arguments]    ${num}
    ${double} =    Evaluate    2 * ${num}
    RETURN    ${double}