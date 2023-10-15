-------------------------------------------------------------------------
-- Create procedures
-------------------------------------------------------------------------
-- Create nuevo_reporte
delimiter $
create procedure create_nuevo_reporte(
    in id_e varchar(20), in id_t varchar(20), in num_rep int, in h_rep decimal(10, 2),
    in res_dom varchar(512), in res_lun varchar(512), in res_mar varchar(512),
    in res_mie varchar(512), in res_jue varchar(512), in res_vie varchar(512)
)
begin
    insert into reportes_semanales values(
        null, id_e, id_t, num_rep, h_rep, "sin aprobar", "sin aprobar", res_dom,
        res_lun, res_mar, res_mie, res_jue, res_vie
    );
end$

-------------------------------------------------------------------------
-- Read procedures
-------------------------------------------------------------------------
-- Read datos_estudiante
delimiter $
create procedure read_datos_estudiante(
    in id_e varchar(20)
)
begin
    select id_tutor, carrera, cantidad_de_reportes,
    horas_acumuladas from estudiante
    where id_estudiante = id_e;
end$

-------------------------------------------------------------------------
-- Update procedures
-------------------------------------------------------------------------
-- Update reporte_especifico
delimiter $
create procedure update_reporte_especifico(
    in id_rep int, in id_e varchar(20), in h_rep decimal(10, 2),
    in res_dom varchar(512), in res_lun varchar(512),
    in res_mar varchar(512), in res_mie varchar(512),
    in res_jue varchar(512), in res_vie varchar(512)
)
begin
    update reportes_semanales set horas_reporte = h_rep, resumen_domingo = res_dom,
    resumen_lunes = res_lun, resumen_martes = res_mar, resumen_miercoles = res_mie,
    resumen_jueves = res_jue, resumen_viernes = res_vie, aprobacion_tutor = "SIN APROBAR", 
    aprobacion_coordinador = "SIN APROBAR"
    where id_reporte = id_rep and id_estudiante = id_e;
end$

-- Update datos_estudiante
delimiter $
create procedure update_datos_estudiante(
    in id_e varchar(20)
)
begin
    update estudiante set
    horas_acumuladas = (
        select sum(horas_reporte)
        as horas_acumuladas
        from reportes_semanales
        where id_estudiante = id_e
        and aprobacion_tutor = "APROBADO"
        and aprobacion_coordinador = "APROBADO"
    ),
    cantidad_de_reportes = (
        SELECT COUNT(*) 
        FROM reportes_semanales 
        WHERE id_estudiante = id_e
    )
    where id_estudiante = id_e;
end$
