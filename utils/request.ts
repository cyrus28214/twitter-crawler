import { headers } from "../config";

export function queryString(params: Record<string, any>) {
    return Object.entries(params).map(([key, value]) => 
        `${key}=${encodeURIComponent(JSON.stringify(value))}`
    ).join('&');
}

export async function get(url: string, params: Record<string, any> = {}) {
    const response = await fetch(`${url}?${queryString(params)}`, {
        headers
    });
    return await response.json();
}