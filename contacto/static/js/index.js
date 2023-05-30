let dataTableC;
let dataTableU;
let dataTableP;
let dataTableR;
let dataTableIsInitializedC= false;
let dataTableIsInitializedU= false;
let dataTableIsInitializedP= false;
let dataTableIsInitializedR= false;

const dataTableOptions = {
    columnDefs:[
        { className: "centered", targets:[0,1,2,3,4,5,6,7,8]},
        {orderable: false, targets:[5]},
        {searchable: false, targets:[5,6,7]}
    ],
    pageLength:4,
    destroy: true
};
/*funcion para iniciar datatable , va a ser asincrono porque va a esperar la lista(list_comunidad) */
const initDataTableC = async () => {
    if (dataTableIsInitializedC){
        dataTableC.destroy();
    }

    await list_comunidad();
    
    dataTableC= $('#datatable-comunidades').DataTable(dataTableOptions);
    dataTableIsInitializedC = true;

};    

const list_comunidad= async() => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_comunidad/");
        const data= await response.json();
        
        let content=``;
        data.comunidades.forEach((comunidad,index)=> {
            content+=`
                <tr>
                    <td>${index}</td>
                    <td>${comunidad.nombre_comunidades}</td>
                    <td>${comunidad.tipo_comunidades}</td>
                    <td>${comunidad.direccion_comunidades}</td>
                    <td>${comunidad.conserje_nombre}</td>
                    <td>${comunidad.fono_comunidadeses}</td>
                    <td>${comunidad.n_unidades}</td>
                    <td>${comunidad.n_residentes}</td>
                    <td>
                       <button class= 'btn btn-sm btn-primary'><i class ='fa-solid fa-pencil'></i></button>
                       <button class= 'btn btn-sm btn-danger'><i class ='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>  
            `;    
        });
        tableBody_comunidades.innerHTML= content;
    } catch (ex) {
        alert(ex);
    }   
          
};

const initDataTableU = async () => {
    if (dataTableIsInitializedU){
        dataTableU.destroy();
    }

    await list_unidad();
    
    dataTableU= $('#datatable-propietario').DataTable(dataTableOptions);
    dataTableIsInitializedU = true;

};

const list_unidad= async() => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_unidad/");
        const data= await response.json();
        
        let content=``;
        data.unidades.forEach((unidad,index)=> {
            content+=`
                <tr>
                    <td>${index}</td>
                    <td>${unidad.n_recinto}</td>
                    <td>${unidad.tipo_unidad}</td>
                    <td>${unidad.nombre_villa}</td>
                    <td>${unidad.direccion_unidad}</td>
                    <td>${unidad.propietario}</td>
                    <td>${unidad.telefono_propietario}</td>
                    <td>${unidad.comunidad}</td>
                    <td>
                       <button class= 'btn btn-sm btn-primary'><i class ='fa-solid fa-pencil'></i></button>
                       <button class= 'btn btn-sm btn-danger'><i class ='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>  
            `;    
        });
        tableBody_unidades.innerHTML= content;
    } catch (ex) {
        alert(ex);
    }   
          
};

const initDataTableP = async () => {
    if (dataTableIsInitializedP){
        dataTableP.destroy();
    }

    await list_propietarios();
    
    dataTableP= $('#datatable-propietarios').DataTable(dataTableOptions);
    dataTableIsInitializedP = true;

};    
const list_propietarios= async() => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_propietarios/");
        const data= await response.json();
        
        let content=``;
        data.propietario.forEach((propietarios,index)=> {
            content+=`
                <tr>
                    <td>${index}</td>
                    <td>${propietarios.rut_propietario}</td>
                    <td>${propietarios.tipo_unidad}</td>
                    <td>${propietarios.direccion}</td>
                    <td>${propietarios.n_recinto}</td>
                    <td>${propietarios.rut_residente}</td>
                    <td>${propietarios.telefono_propietario}</td>
                    <td>${propietarios.estado}</td>
                    <td>
                       <button class= 'btn btn-sm btn-primary'><i class ='fa-solid fa-pencil'></i></button>
                       <button class= 'btn btn-sm btn-danger'><i class ='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>  
            `;    
        });
        tableBody_propietarios.innerHTML= content;
    } catch (ex) {
        alert(ex);
    }   
          
};

const initDataTableR = async () => {
    if (dataTableIsInitializedR){
        dataTableR.destroy();
    }

    await list_residentes();
    
    dataTableR= $('#datatable-residentes').DataTable(dataTableOptions);
    dataTableIsInitializedR = true;

};    
const list_residentes= async() => {
    try {
        const response = await fetch("http://127.0.0.1:8000/list_residentes/");
        const data= await response.json();
        
        let content=``;
        data.residente.forEach((residentes,index)=> {
            content+=`
                <tr>
                    <td>${index}</td>
                    <td>${residentes.rut_residente}</td>
                    <td>${residentes.tipo_unidad}</td>
                    <td>${residentes.direccion}</td>
                    <td>${residentes.n_recinto}</td>
                    <td>${residentes.rut_propietario}</td>
                    <td>${residentes.telefono_residente}</td>
                    <td>${residentes.estado}</td>
                    <td>
                       <button class= 'btn btn-sm btn-primary'><i class ='fa-solid fa-pencil'></i></button>
                       <button class= 'btn btn-sm btn-danger'><i class ='fa-solid fa-trash-can'></i></button>
                    </td>
                </tr>  
            `;    
        });
        tableBody_residentes.innerHTML= content;
    } catch (ex) {
        alert(ex);
    }   
          
};

window.addEventListener("load", async() => {
    await initDataTableC();
    await initDataTableU();
    await initDataTableP();
    await initDataTableR();
});