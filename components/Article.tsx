import { Card, CardFooter } from "@/components/ui/card";
import { CalendarIcon, ExternalLinkIcon } from "lucide-react";
import { Article } from "@/types";
import { formatDate } from "@/lib/utils";

interface ArticleComponentProps {
  article: Article;
}

export default function ArticleComponent({ article }: ArticleComponentProps): JSX.Element {
  // Format date if article has a timestamp
  const formattedDate: string | null = article.created_at 
    ? formatDate(article.created_at)
    : null;

  return (
    <Card className="transition-all hover:shadow-md">
      <div className="p-4 flex flex-col h-full">
        <div className="flex-1">
          <h3 className="font-medium text-lg mb-2 line-clamp-2 hover:text-primary transition-colors">
            <a 
              href={article.link} 
              target="_blank" 
              rel="noopener noreferrer"
              className="hover:underline"
            >
              {article.title}
            </a>
          </h3>
          
          <div className="flex items-center text-xs text-muted-foreground mt-2">
            <div className="w-1 h-1 bg-muted-foreground rounded-full mr-2"></div>
            <div className="flex items-center">
              {formattedDate && (
                <>
                  <CalendarIcon className="h-3 w-3 mr-1" />
                  <span>{formattedDate}</span>
                </>
              )}
            </div>
          </div>
        </div>
        
        <CardFooter className="px-0 pt-4 pb-0 flex justify-end">
          <a 
            href={article.link} 
            target="_blank" 
            rel="noopener noreferrer"
            className="text-xs flex items-center font-medium text-primary hover:underline"
          >
            Visit link <ExternalLinkIcon className="ml-1 h-3 w-3" />
          </a>
        </CardFooter>
      </div>
    </Card>
  );
}