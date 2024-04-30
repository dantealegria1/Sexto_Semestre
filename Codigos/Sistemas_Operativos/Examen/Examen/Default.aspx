<%@ Page Title="Home Page" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Examen._Default" %>

<asp:Content ID="BodyContent" ContentPlaceHolderID="MainContent" runat="server">
<header>
    <div>
        <h1>Administrador de Procesos</h1>
    </div>
    <div>
        <div class="container">
            <h2>Informacion de los procesos</h2>
            <asp:Table ID="tablaProcesos" runat="server">
                <asp:TableRow>
                    <asp:TableCell>Proceso</asp:TableCell>
                    <asp:TableCell>Largo de Proceso</asp:TableCell>
                    <asp:TableCell>Prioridad</asp:TableCell>
                </asp:TableRow>
            </asp:Table>
             <button id="addbutton" runat="server" OnClick="btnAgregar_Click">Agregar Proceso</button>

        </div>
    </div>
</header>
</asp:Content>
    