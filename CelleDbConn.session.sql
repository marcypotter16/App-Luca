ALTER TABLE celle
ADD COLUMN riga INTEGER;

ALTER TABLE celle
ADD COLUMN colonna INTEGER;

SELECT * FROM freezers;
SELECT * FROM celle;
SELECT * FROM scatole;

DELETE FROM scatole WHERE 1;
DELETE FROM celle WHERE 1;

INSERT INTO scatole (in_freezer, nome) VALUES (1, 'scatola test');

SELECT * FROM celle WHERE id = 8