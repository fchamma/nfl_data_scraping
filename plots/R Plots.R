names(yards_winning_team)
plot(yards_winning_team, pch=16)
lines(yards_winning_team)
ggplot2
yards_winning_team$alpha = c(rep(1,16), 0)
library(grid)

plot = ggplot(data=yards_winning_team, aes(V1, V2)) + xlab("") + ylab("")


plot +  theme(panel.background = element_rect(fill = "transparent"), 
        plot.background = element_rect(fill = "transparent"), 
        panel.grid.minor = element_line(colour = "transparent"), 
        panel.grid.major = element_line(colour = "transparent"),
        axis.ticks = element_line(colour = "black"),
        rect = element_rect(colour = "transparent"),
        axis.text = element_text(colour="transparent")) +
  geom_line(size=2, colour="#db4249",arrow = arrow(type = "closed")) + 
  geom_point(size=5, colour="#db4249", data=yards_winning_team[2:17, ]) + 
  scale_x_continuous(breaks=0) + 
  scale_y_continuous(breaks=0) + theme(panel.border = element_rect(colour="black"))




ggsave("yards-years-line.pdf", width=15, height=8)

plot + geom_line(size=2, colour="transparent",arrow = arrow(type = "closed")) + 
  geom_point(size=5, colour="transparent", data=yards_winning_team[2:17, ]) + 
  scale_x_continuous(breaks=1998:2014) + scale_y_continuous(breaks=seq(340,400,10)) +
  theme(panel.background = element_rect(fill = "transparent"), 
          plot.background = element_rect(fill = "transparent"), 
          panel.grid.minor = element_line(colour = "grey20"), 
          panel.grid.major = element_line(colour = "grey30", size = 0.2))
ggsave("yards-years-blank.pdf", width=15, height=8)

