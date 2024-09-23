Dentro das pastas, você vai encontrar os fits e imagens finais que utilizei na minha análise.

Também vai encontrar um notebook chamado teste fluxos, que testa se os fluxos e magnitudes estão sendo preservados e um chamado diagramas tipo UVJ, onde estou construindo os diagramas.

Abaixo segue como obter a magnitude com os três instrumentos que utilizei:

Sptizer:
m = -2.5 log_10 (contagens * 2.35 * 10^-5 / 280.9)
        
CANGA:
m = -2.5 log_10 (contagens) + Zero Point  (do header)

GALEX:
m = -2.5 log_10(contagens) + Zero Point 20.08 (NUV) 18.82 (FUV))

Mais referências podem ser encontradas no meu relatório final, também nessa pasta.