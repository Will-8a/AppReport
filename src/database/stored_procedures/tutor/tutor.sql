-------------------------------------------------------------------------
-- Read procedures
-------------------------------------------------------------------------
-- Read reportes_estudiante (tutor)
delimiter $
create procedure read_reportes_estudiante_tutor(
    in id_es varchar(20), in id_t varchar(20)
)
begin
    select * from reportes_semanales
    where id_estudiante = id_es
    and id_tutor = id_t;
end$

-- Read estudiantes tutorados()
delimiter $
create procedure read_estudiantes_tutorados(
    in id_t varchar(20)
)
begin
    select cedula, nombre_1, nombre_2, apellido_p,
    apellido_m, email, tipo_de_usuario,
    cantidad_de_reportes, horas_acumuladas
    from usuario, estudiante where cedula in (
        select id_estudiante from tutor
        where id_tutor = id_t
    )
    GROUP by cedula;
end$

-------------------------------------------------------------------------
-- Update procedures
-------------------------------------------------------------------------
-- Update estatus_reporte (tutor)
delimiter $
create procedure update_estatus_reporte_tutor(
    in estatus varchar(12), in id_r int, in id_t varchar(20)
)
begin
    update reportes_semanales set aprobacion_tutor = estatus
    where id_reporte = id_r and id_tutor = id_t;
end$
