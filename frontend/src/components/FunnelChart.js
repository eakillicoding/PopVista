import React, { useState, useEffect } from "react";
import {BarChart, Bar, XAxis, YAxis, ResponsiveContainer, Label, CartesianGrid, Tooltip} from 'recharts';


const FunnelChart = () => {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/countries/population/');
            if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const jsonData = await response.json();
            const populationData = jsonData[0]['population_data'];
            const updatedData = populationData.map(item => ({
                ...item,
                male: item.male > 0 ? -item.male : item.male
            }));
            setData(updatedData);
        } catch (error) {
            console.error("Fetching data failed:", error);
        }
    };

    fetchData();
}, []);

    const customTooltip = (value, name) => {
        const val = Math.abs(value);
        return [`${val.toFixed(2)}%`, name];
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '800px' }}>
            <div style={{ width: '800px', height: '450px', border: '2px solid #8e8e8e', borderRadius: '5px', padding: '90px', color: '#636363', textAlign: 'center', marginBottom: '80px'}}>
            <h3>US Population (2022)</h3>
            <ResponsiveContainer>
                <BarChart
                layout="vertical"
                data={data}
                margin={{ top: 30, right: 20, left: 20, bottom: 15 }}
                barCategoryGap={1}
                barGap={-32}
                >
                <CartesianGrid vertical={true} horizontal={false}/>
                <XAxis
                    type="number"
                    allowDecimals={false}
                    domain={[-8, 8]}
                    ticks={[-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8]}
                    tickFormatter={(tick) => Math.abs(tick)}
                    axisLine={false}
                    tickLine={false}
                >
                    <Label value="Percentage of Population" offset={-10} position="insideBottom" />
                </XAxis>
                <Tooltip formatter={customTooltip}/>
                <YAxis
                    dataKey="age"
                    type="category"
                    axisLine={false}
                    tickLine={false}
                >
                    <Label value="Age Group" angle={-90} offset={-10} position='insideLeft' />
                </YAxis>
                <Bar dataKey="male" fill="#6fa8dc" stroke="#000000" strokeWidth={.5}/>
                <Bar dataKey="female" fill="#d5a6bd" stroke="#000000" strokeWidth={.5}/>
                </BarChart>
            </ResponsiveContainer>
            </div>
        </div>
        );
    }

export default FunnelChart;
