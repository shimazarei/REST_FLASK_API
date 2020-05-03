USE DB1;

DELETE FROM DB1.node_tree_name;

DELETE FROM DB1.node_tree;

INSERT INTO DB1.node_tree(iNode,level,iLeft,iRight) VALUES ('1','2','2','3'),('2','2','4','5') ,('3','2','6','7'),('4','2','8','9'),('5','1','1','24'),('6','2','10','11'),('7','2','12','19'),('8','3','15','16'),('9','3','17','18'),('10','2','20','21'),('11','3','13','14'),('12','2','22','23');


INSERT INTO DB1.node_tree_name(iNode, Language, nodeName) VALUES ('1','english','marketing'),('1','italian','marketing'),('2','english','helpdesk'),('2','italian','supporto tecnico'),('3','english','managers'),('3','italian','managers'),('4','english','customer account'),('4','italian','assistenza cliente'),('5','english','docebo'),('5','italian','docebo'),('6','english','accounting'),('6','italian','amministrazzione'),('7','english','sales'),('7','italian','supporto vendito'),('8','english','italy'),('8','italian','italia'),('9','english','europe'),('9','italian','europa'),('10','english','developers'),('10','italian','sviluppatori'),('11','english','north america'),('11','italian','north america'),('12','english','quality assurance'),('12','italian','controllo qualita');

