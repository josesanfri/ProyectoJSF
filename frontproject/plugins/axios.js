import Cookies from 'js-cookie'

export default function ({ $axios, redirect, store, req }, inject) {
    let errorsDic = {
        400: 'Datos incorrectos, revise los datos introducidos.',
        401: 'No has iniciado sesión. Inicia sesión o créate una cuenta.',
        404: 'El recurso que solicitas no existe, vuélvelo a intentar.',
        500: 'No podemos ayudarte, vuélvalo a intentar.'
    }

    // UTILS
    let badResponse = function(error) {
        if(error.status in errorsDic && !error?.data?.message) {
        store.commit('message/addItem', {
                text: errorsDic[error.status],
                icon: {
                    image: {
                        src: '/icon/base/black/triangle-exclamation.webp',
                        alt: 'triangle exclamation icon',
                        width: 30,
                        height: 30,
                        attrs: {
                        needContrast: true
                        }
                    }, 
                    sources: [{
                        srcset: '/icon/base/black/triangle-exclamation.webp',
                        media:'(min-width: 320px)',
                    }]
                },
                reference: new Date().getTime().toString(),
                type: {
                    isWarning: true
                }
            })
        } else {
        store.commit('message/addItem', {
                text: error.data.message,
                reference: new Date().getTime().toString(),
                icon: {
                    image: {
                        src: '/icon/base/black/xmark.webp',
                        alt: 'cross icon',
                        width: 30,
                        height: 30,
                        attrs: {
                        needContrast: true
                        }
                    }, 
                    sources: [{
                        srcset: '/icon/base/black/xmark.webp',
                        media:'(min-width: 320px)',
                    }]
                },
                type: {
                    isDanger: true
                }
            })
        }
        return false
    }

    // CODE  
    const API = $axios.create({
        baseURL: 'http://localhost:8000/api/',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })

    API.interceptors.request.use(function(config) {
        if(!config.headers.Authorization && store.state.auth.user?.token) {
            config.headers.Authorization = store.state.auth.user?.token
        }

        return config
    }, function(err) {
        return Promise.reject(err);
    })


    API.onResponse(res => {
        let {message, ...data} = res.data

        if(message && message.length > 0) {
        store.commit('message/addItem', {
            text: message,
            reference: new Date().getTime().toString(),
            icon: {
                image: {
                    src: '/icon/base/black/check.webp',
                    alt: 'check icon',
                    width: 30,
                    height: 30,
                    attrs: {
                    needContrast: true
                    }
                }, 
                sources: [{
                    srcset: '/icon/base/black/check.webp',
                    media:'(min-width: 320px)',
                }]
            }, 
            type: {
                isSuccess: true
            }
        })
        
        return data
        }

    })

    API.onError(error => {
        if (error.response.status === 500) {
        badResponse(error.response)
        }
        else {
        badResponse(error.response)
        }
    })

    inject('axiosAPI', API)
}