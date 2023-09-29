/* ModeloLógico: */

CREATE TABLE Cliente (
    idCliente Integer PRIMARY KEY,
    nmCliente varchar(200),
    email varchar(300)
);

CREATE TABLE Pedido (
    idPedido Integer PRIMARY KEY,
    dtPedido date,
    totalPagar float,
    fk_Cliente_idCliente Integer
);

CREATE TABLE Produto (
    valUnitario float,
    nmProduto varchar(300),
    idProduto Integer PRIMARY KEY
);

CREATE TABLE Item (
    fk_Produto_idProduto Integer,
    fk_Pedido_idPedido Integer
);
 
ALTER TABLE Pedido ADD CONSTRAINT FK_Pedido_2
    FOREIGN KEY (fk_Cliente_idCliente)
    REFERENCES Cliente (idCliente)
    ON DELETE RESTRICT;
 
ALTER TABLE Item ADD CONSTRAINT FK_Item_1
    FOREIGN KEY (fk_Produto_idProduto)
    REFERENCES Produto (idProduto)
    ON DELETE RESTRICT;
 
ALTER TABLE Item ADD CONSTRAINT FK_Item_2
    FOREIGN KEY (fk_Pedido_idPedido)
    REFERENCES Pedido (idPedido)
    ON DELETE SET NULL;