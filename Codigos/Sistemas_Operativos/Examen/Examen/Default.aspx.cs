using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Web;
using System.Web.Services.Description;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Examen
{
    public partial class _Default : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if(!IsPostBack)
            {
                Cargarddl();
            }
        }

        protected void Cargarddl()
        {
            //Cargamos los valores del 1-10
            
        }
        protected void btnAgregar_Click(object sender, EventArgs e)
        {
            AgregarFila();
        }

        private void AgregarFila()
        {
            TableRow fila = new TableRow();

            // Añade celdas a la fila
            TableCell celdaProceso = new TableCell();
            celdaProceso.Text = "Nuevo Proceso"; // Puedes cambiar esto por el valor deseado
            fila.Cells.Add(celdaProceso);

            TableCell celdaLargoProceso = new TableCell();
            celdaLargoProceso.Text = "Nuevo Largo"; // Puedes cambiar esto por el valor deseado
            fila.Cells.Add(celdaLargoProceso);

            TableCell celdaPrioridad = new TableCell();
            celdaPrioridad.Text = "Nueva Prioridad"; // Puedes cambiar esto por el valor deseado
            fila.Cells.Add(celdaPrioridad);

            // Agrega la fila a la tabla
            tablaProcesos.Rows.Add(fila);
        }

    }
}