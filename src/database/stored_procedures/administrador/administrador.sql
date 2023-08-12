-------------------------------------------------------------------------
-- Create procedures
-------------------------------------------------------------------------
-- Create usuario_estudiante
delimiter $
create procedure create_usuario_estudiante(
    in ced varchar(20), in nom1 varchar(32), in nom2 varchar(32),
    in app varchar(32), in apm varchar(32), in e_mail varchar(45),
    in con char(105), in tu varchar(20), in id_t varchar(20),
    in car varchar(64), in can_r int, in horas_a decimal(10, 2)
)
begin
    insert into usuario values (ced, nom1, nom2, app, apm, e_mail, con, tu);
    insert into estudiante values(ced, id_t, car, can_r, horas_a);
    insert into tutor values (id_t, ced);
end$