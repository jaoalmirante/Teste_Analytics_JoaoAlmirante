-- Soma total de vendas por produto e ordenação
SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM 
    NomeDaTabela
GROUP BY 
    Produto, Categoria
ORDER BY 
    Total_Vendas DESC;

-- Identificação de produtos com menor venda no mês de junho de 2024
SELECT 
    Produto,
    Categoria,
    SUM(Quantidade * Preço) AS Total_Vendas
FROM 
    NomeDaTabela
WHERE 
    YEAR(Data) = 2024 AND MONTH(Data) = 6
GROUP BY 
    Produto, Categoria
ORDER BY 
    Total_Vendas ASC
LIMIT 1;
