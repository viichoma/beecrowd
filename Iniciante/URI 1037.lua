/* https://www.beecrowd.com.br/judge/pt/problems/view/1037 */

A = tonumber(io.read())
if A<0 or A>100.0 then
    print("Fora de intervalo") 
elseif (A<=25.0) then
    print("Intervalo [0,25]") 
elseif(A<=50.0) then
    print("Intervalo (25,50]") 
elseif(A<=75.0) then
    print("Intervalo (50,75]") 
elseif(A<=100.0) then
    print("Intervalo (75,100]") end