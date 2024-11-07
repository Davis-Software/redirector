import React from "react";
import PageBase from "./PageBase";
import SettingsType from "../types/settingsType";
import {useEffect, useState} from "react";
import {Button} from "@mui/material";

function Settings(){
    const settingsListRef = React.createRef<HTMLUListElement>()
    const [settings, setSettings] = useState<SettingsType | null>(null)

    useEffect(() => {
        fetch("/api/settings")
            .then(res => res.json())
            .then(setSettings)
    }, []);

    function handleSave(){
        if(!settingsListRef.current) return
        const inputs = settingsListRef.current.querySelectorAll("input")

        const formData = new FormData()
        inputs.forEach(input => {
            formData.append(input.name, input.value)
        })

        fetch("/api/settings", {
            method: "POST",
            body: formData
        })
    }

    return (
        <PageBase>
            {settings ? (
                <ul ref={settingsListRef}>
                    {Object.entries(settings).map(([key, value]) => (
                        <li key={key}>{key}: <input
                            type="text"
                            name={key}
                            value={value || ""}
                            onChange={e => setSettings(s => ({...s, [key]: e.target.value}))}
                        /></li>
                    ))}
                </ul>
            ) : "Loading..."}

            <Button variant="contained" color="primary" onClick={handleSave}>Save</Button>
        </PageBase>
    )
}

export default Settings