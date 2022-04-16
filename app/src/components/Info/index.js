import React from 'react';
import { useParams } from 'react-router-dom';

const Info = () => {
    const { id } = useParams();
    return (
        <div className="App">
            <header className="App-header">
                <h1>Evento Fibom + 321 Click</h1>
                <h2>Informacion</h2>

                {/* create a list that contains all the info of the fireman */}
                <ul>
                    <li>Nombre: Sebastian Diaz</li>
                    <li>Mail: <span>sdiazdelafuente9@gmail.com</span></li>
                    <li>Cuerpo de Bomberos: 18 de Santiago</li>
                    <li>Cargo: Brigadier</li>
                </ul>
            </header>
        </div>
    );
}

export default Info;