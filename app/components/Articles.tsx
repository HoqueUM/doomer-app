"use client";
import { useState, useEffect } from 'react'
import { Article } from '../types'
import ArticleComponent from './Article'

export default function Articles() {
    const [articles, setArticles] = useState<Article[]>([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {

        fetch('/api/get_news')
            .then(res => res.json())
            .then(data => {
                setArticles(data)
                setLoading(false)
            })
    }, [])

    return (
        <div className="container mx-auto">
            <div>{loading ? ('Loading...') : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {articles.reverse().map(article => (
                        <ArticleComponent key={article.id} article={article} />
                    ))}
                    </div>
                )}

            </div>
        </div>
    )
}